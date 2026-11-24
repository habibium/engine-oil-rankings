(function () {
  "use strict";

  var RANKINGS = [
    { id: "protection", label: "Protection" },
    { id: "performance", label: "Performance" },
    { id: "value", label: "Value for money" }
  ];
  var GROUP_START = { sport_score: 1, price: 1, kv40: 1, city_km: 1 };
  var repo = document.body.getAttribute("data-repo");
  var cache = {};
  var grades = [];
  var state = { grade: null, rank: "protection", type: "all", q: "", sort: "rank", dir: "asc" };

  var $ = function (id) { return document.getElementById(id); };

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (attrs[k] == null || attrs[k] === false) return;
      if (k === "text") n.textContent = attrs[k];
      else if (k === "class") n.className = attrs[k];
      else if (k.slice(0, 2) === "on") n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c != null) n.append(c); });
    return n;
  }

  function readHash() {
    var p = new URLSearchParams(location.hash.slice(1));
    ["grade", "rank", "type", "sort", "dir"].forEach(function (k) { if (p.get(k)) state[k] = p.get(k); });
    if (!RANKINGS.some(function (r) { return r.id === state.rank; })) state.rank = "protection";
    if (state.dir !== "desc") state.dir = "asc";
  }

  function writeHash() {
    var p = new URLSearchParams();
    p.set("grade", state.grade);
    p.set("rank", state.rank);
    if (state.type !== "all") p.set("type", state.type);
    if (state.sort !== "rank") { p.set("sort", state.sort); p.set("dir", state.dir); }
    history.replaceState(null, "", "#" + p.toString());
  }

  function getJSON(url) {
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error(url + ": " + r.status);
      return r.json();
    });
  }

  function loadGrade(slug) {
    if (!cache[slug]) cache[slug] = getJSON("data/" + slug + ".json");
    return cache[slug];
  }

  function segmented(container, items, current, onPick) {
    container.replaceChildren.apply(container, items.map(function (it) {
      return el("button", {
        type: "button", text: it.label, "aria-pressed": String(it.id === current),
        onclick: function () { onPick(it.id); }
      });
    }));
  }

  function setSort(key) {
    if (state.sort === key) state.dir = state.dir === "asc" ? "desc" : "asc";
    else { state.sort = key; state.dir = "asc"; }
    render();
  }

  function compareBy(g, ranking) {
    var pos = {};
    ranking.order.forEach(function (id, i) { pos[id] = i; });
    var sign = state.dir === "asc" ? 1 : -1;
    var value = function (o) {
      if (state.sort === "rank") return ranking.rank[o.id];
      if (state.sort === "name") return o.name.toLowerCase();
      var c = o.cells[state.sort];
      return c ? c.v : null;
    };
    return function (a, b) {
      var va = value(a), vb = value(b);
      // Missing values stay at the bottom whichever way the column is sorted.
      if (va == null && vb != null) return 1;
      if (vb == null && va != null) return -1;
      if (va != null && vb != null && va !== vb) return (va < vb ? -1 : 1) * sign;
      return pos[a.id] - pos[b.id];
    };
  }

  function headCell(key, label, unit, cls) {
    var active = state.sort === key;
    var arrow = active ? (state.dir === "asc" ? "▲" : "▼") : "↕";
    return el("th", {
      class: cls, scope: "col",
      "aria-sort": active ? (state.dir === "asc" ? "ascending" : "descending") : null
    }, [
      el("button", {
        type: "button", onclick: function () { setSort(key); },
        title: "Sort by " + label + (active && state.dir === "asc" ? " (descending)" : " (ascending)")
      }, [
        el("span", { class: "h-label" }, [label, el("span", { class: "arrow", "aria-hidden": "true", text: arrow })]),
        unit ? el("span", { class: "h-unit", text: unit }) : null
      ])
    ]);
  }

  function sheetLinks(o) {
    if (!o.datasheets.length) return null;
    return el("div", { class: "sheets" }, o.datasheets.map(function (href) {
      var safety = /(^|[-_])sds([-_.]|$)/.test(href.split("/").pop());
      return el("a", { href: href, target: "_blank", rel: "noopener", text: safety ? "Safety data sheet" : "Datasheet" });
    }));
  }

  function render() {
    var g = cache[state.grade + ":data"];
    if (!g) return;
    var ranking = g.rankings[state.rank];
    if (state.type !== "all" && !g.types.some(function (t) { return t.id === state.type; })) state.type = "all";
    if (state.sort !== "rank" && state.sort !== "name" && !g.columns.some(function (c) { return c.key === state.sort; })) state.sort = "rank";

    document.title = g.grade + " motorcycle oil rankings";
    $("title").textContent = ranking.title;
    $("lede").textContent = ranking.lede;
    $("caption").textContent = ranking.title;

    segmented($("grade"), grades.map(function (x) { return { id: x.slug, label: x.grade }; }), state.grade, function (slug) {
      state.grade = slug; state.sort = "rank"; state.dir = "asc"; start();
    });
    segmented($("ranking"), RANKINGS, state.rank, function (id) {
      state.rank = id; state.sort = "rank"; state.dir = "asc"; render();
    });
    segmented($("type"), [{ id: "all", label: "All" }].concat(g.types), state.type, function (id) {
      state.type = id; render();
    });

    $("picks").replaceChildren.apply($("picks"), ranking.picks.map(function (p) {
      return el("div", { class: "pick" }, [el("b", { text: p.label + ": " }), p.name]);
    }));

    var head = el("tr", {}, [
      headCell("rank", "#", "this ranking", "c-rank"),
      headCell("name", "Engine oil", g.grade + ", 1 L", "c-name")
    ].concat(g.columns.map(function (c) {
      return headCell(c.key, c.label, c.unit, GROUP_START[c.key] ? "col-start" : null);
    })));
    $("table").tHead.replaceChildren(head);

    var q = state.q.trim().toLowerCase();
    var rows = g.oils.filter(function (o) {
      return (state.type === "all" || o.type === state.type) && (!q || (o.name + " " + o.sub).toLowerCase().indexOf(q) !== -1);
    }).sort(compareBy(g, ranking));

    var body = rows.map(function (o) {
      var rank = ranking.rank[o.id];
      var badge = rank == null ? "ref" : rank <= 3 ? "top" : "rest";
      return el("tr", {}, [
        el("td", { class: "c-rank" }, [el("div", { class: "rank " + badge, text: rank == null ? "–" : String(rank), title: rank == null ? "Not ranked: no datasheet" : null })]),
        el("th", { class: "c-name", scope: "row" }, [
          el("div", { class: "name", text: o.name }),
          el("span", { class: "sub", text: o.sub }),
          sheetLinks(o)
        ])
      ].concat(g.columns.map(function (c) {
        var cell = o.cells[c.key];
        var cls = [cell.m, cell.t === "—" ? "na" : null, GROUP_START[c.key] ? "col-start" : null].filter(Boolean).join(" ");
        return el("td", { class: cls || null }, [cell.t, cell.sub ? el("span", { class: "sub", text: cell.sub }) : null]);
      })));
    });
    if (!body.length) {
      body = [el("tr", { class: "empty" }, [el("td", { colspan: String(g.columns.length + 2), text: "No oil matches. Clear the search or pick another oil type." })])];
    }
    $("table").tBodies[0].replaceChildren.apply($("table").tBodies[0], body);
    $("count").textContent = "Showing " + rows.length + " of " + g.oils.length + " " + g.grade + " oils · prices " + g.updated + ", " + g.region;

    $("downloads").replaceChildren(
      el("span", { class: "muted", text: "This ranking as a file:" }),
      el("a", { class: "btn", href: ranking.pdf, target: "_blank", rel: "noopener", text: "PDF (sharp, for reading)" }),
      el("a", { class: "btn", href: ranking.png, target: "_blank", rel: "noopener", text: "PNG (for sharing)" }),
      el("a", { class: "btn", href: "data/" + g.slug + ".json", target: "_blank", rel: "noopener", text: "All data (JSON)" })
    );
    $("note-prices").textContent = g.notes.prices;
    $("note-excluded").textContent = g.notes.excluded;
    $("sources").textContent = "Sources: " + g.sources;
    writeHash();
  }

  function start() {
    $("lede").textContent = "Loading…";
    return loadGrade(state.grade).then(function (g) {
      cache[state.grade + ":data"] = g;
      render();
    }).catch(function (e) {
      $("lede").textContent = "Couldn't load the data (" + e.message + "). Try reloading the page.";
    });
  }

  var searchTimer;
  $("search").addEventListener("input", function (e) {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () { state.q = e.target.value; render(); }, 80);
  });

  getJSON("data/grades.json").then(function (list) {
    grades = list;
    readHash();
    if (!grades.some(function (x) { return x.slug === state.grade; })) state.grade = grades[0].slug;
    return start();
  }).catch(function (e) {
    $("lede").textContent = "Couldn't load the data (" + e.message + "). Try reloading the page.";
  });

  if (repo) {
    getJSON("https://api.github.com/repos/" + repo).then(function (r) {
      if (typeof r.stargazers_count !== "number" || r.stargazers_count < 1) return;
      var c = $("star-count");
      c.textContent = r.stargazers_count.toLocaleString("en");
      c.setAttribute("aria-label", r.stargazers_count + " stars");
      c.hidden = false;
    }).catch(function () {});
  }
})();
