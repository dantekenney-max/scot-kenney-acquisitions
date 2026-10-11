/* Scot Kenney Acquisitions — site behaviour
   - mobile navigation toggle
   - scroll reveal
   - contact form: posts to the configured relay endpoint; if none is configured
     yet, falls back to a pre-filled email so no inquiry is lost. */
(function () {
  "use strict";

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("nav-locked", open);
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-locked");
      });
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Contact form ---------- */
  var form = document.getElementById("contact-form");
  if (!form) return;

  // Pre-select the topic when arriving from a CTA (e.g. contact/?topic=property)
  try {
    var params = new URLSearchParams(window.location.search);
    var topic = params.get("topic");
    var select = form.querySelector('select[name="topic"]');
    if (topic && select) {
      var map = { capital: "Capital / Joint Venture Partnership", property: "Property for Sale", brokerage: "Brokerage Opportunity", development: "Development Collaboration", other: "Other" };
      if (map[topic]) select.value = map[topic];
    }
  } catch (e) { /* ignore */ }

  var status = document.getElementById("form-status");
  var endpoint = (form.getAttribute("data-endpoint") || "").trim();
  var destination = form.getAttribute("data-destination") || "";
  var submitBtn = form.querySelector('button[type="submit"]');

  function showStatus(kind, html) {
    status.className = "form-status " + kind;
    status.innerHTML = html;
    status.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();

    // Honeypot: real visitors never fill this.
    if (form.querySelector('input[name="_honey"]').value) { return; }

    if (!form.checkValidity()) { form.reportValidity(); return; }

    var data = new FormData(form);
    var confirmation = "Thank you for reaching out. We will review your message and respond if there is a potential fit.";

    if (!endpoint) {
      // No relay configured yet: open a pre-filled email to the verified destination.
      var body = [
        "Name: " + data.get("name"),
        "Organization: " + (data.get("organization") || "-"),
        "Email: " + data.get("email"),
        "Telephone: " + (data.get("telephone") || "-"),
        "Regarding: " + data.get("topic"),
        "",
        data.get("message")
      ].join("\n");
      var href = "mailto:" + destination + "?subject=" + encodeURIComponent("Website inquiry: " + data.get("topic")) + "&body=" + encodeURIComponent(body);
      window.location.href = href;
      showStatus("ok", confirmation + " Your email application should now open with your message ready to send.");
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = "Sending…";
    fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
      .then(function (r) {
        if (!r.ok) throw new Error("Request failed");
        form.reset();
        showStatus("ok", confirmation);
      })
      .catch(function () {
        showStatus("err", "Your message could not be sent. Please email <a href=\"mailto:" + destination + "\">" + destination + "</a> directly.");
      })
      .finally(function () {
        submitBtn.disabled = false;
        submitBtn.textContent = "Send Inquiry";
      });
  });
})();
