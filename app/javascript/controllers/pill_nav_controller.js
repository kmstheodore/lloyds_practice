import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["pill", "panel", "navItem"]

  select(event) {
    event.preventDefault()
    const clicked = event.currentTarget
    const tabName = clicked.dataset.tab

    this.pillTargets.forEach((pill) => {
      const isSelected = pill === clicked
      pill.classList.toggle("bg-[#141716]", isSelected)
      pill.classList.toggle("text-white", isSelected)
      pill.classList.toggle("border-[#141716]", isSelected)

      pill.classList.toggle("bg-white", !isSelected)
      pill.classList.toggle("text-[#141716]", !isSelected)
      pill.classList.toggle("border-[#2A2F2D]", !isSelected)
    })

    this.showPanel(tabName)
    clicked.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" })
  }

  switchBottomNav(event) {
    event.preventDefault()
    const clicked = event.currentTarget
    const tabName = clicked.dataset.tab

    this.navItemTargets.forEach((item) => {
      const isSelected = item === clicked
      const indicator = item.querySelector("[data-nav-indicator]")

      item.classList.toggle("font-bold", isSelected)
      item.classList.toggle("text-[#141716]", isSelected)
      item.classList.toggle("font-medium", !isSelected)
      item.classList.toggle("text-[#5C6260]", !isSelected)

      if (indicator) {
        indicator.classList.toggle("hidden", !isSelected)
      }
    })

    if (tabName === "home") {
      const activePill = this.pillTargets.find((p) => p.classList.contains("bg-[#141716]"))
      this.showPanel(activePill ? activePill.dataset.tab : "summary")
    } else {
      this.showPanel(tabName)
    }

    window.scrollTo({ top: 0, behavior: "smooth" })
  }

  toggleRow(event) {
    const button = event.currentTarget
    const detailsId = button.getAttribute("aria-controls")
    const details = document.getElementById(detailsId)
    const icon = button.querySelector("[data-plus-icon]")

    if (!details) return

    const willOpen = details.classList.contains("hidden")
    details.classList.toggle("hidden", !willOpen)
    button.setAttribute("aria-expanded", willOpen ? "true" : "false")

    if (icon) {
      icon.textContent = willOpen ? "−" : "+"
    }
  }

  showPanel(tabName) {
    const homeTabs = ["summary", "everyday", "save_invest", "borrow", "homes", "insure"]
    const isHomeTab = homeTabs.includes(tabName)

    this.panelTargets.forEach((panel) => {
      if (panel.dataset.tab === "home-header") {
        panel.classList.toggle("hidden", !isHomeTab)
      } else {
        panel.classList.toggle("hidden", panel.dataset.tab !== tabName)
      }
    })
  }
}
