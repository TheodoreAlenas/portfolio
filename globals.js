
const colorScheme = {

    localStoragePrefix: 'portfolioColorScheme',

    init: function() {
        const prefersDark  = window.matchMedia('(prefers-color-scheme: dark)').matches
        const prefersContr = window.matchMedia('(prefers-contrast: more)').matches
        const preferredNow = prefersDark ? (prefersContr ? 'contr' : 'dark') : 'light'

        const p = this.localStoragePrefix
        const lastPreferred = localStorage.getItem(p + 'LastPreferred')
        const last = localStorage.getItem(p + 'LastUsed')
        localStorage.setItem(p + 'LastPreferred', preferredNow)

        if (lastPreferred === preferredNow && last)
            this.set(last)
        else
            this.set(preferredNow)
    },

    set: function(value) {
        let lightDark = value
        if (value === 'contr') lightDark = 'dark'
        const html = document.querySelector('html')
        html.style.colorScheme = lightDark
        html.setAttribute('data-sch', value)
        localStorage.setItem(this.localStoragePrefix + 'LastUsed', value)
    },

    initInputs: function(query) {
        const themeRadios = document.querySelectorAll(query);
        const sch = document.querySelector("html").getAttribute("data-sch");
        for (let r of themeRadios) {
            const v = r.getAttribute("value")
            if (v == sch) r.checked = true;
            const me = this
            r.onchange = function(_) {me.set(v)}
        }
    }
}
