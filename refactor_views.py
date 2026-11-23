from pathlib import Path

source_path = Path("app/views/home/index.html.erb")
source = source_path.read_text()

def extract(start_marker, end_marker):
    start = source.find(start_marker)
    end = source.find(end_marker)

    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not find markers: {start_marker!r}")

    return source[start:end]

# Extract each original section without changing its HTML.
top_navigation = extract(
    "    <!-- Top Header for Home / Pill Tabs -->",
    "    <!-- SUMMARY TAB VIEW -->"
)

summary = extract(
    "    <!-- SUMMARY TAB VIEW -->",
    "    <!-- EVERYDAY TAB VIEW -->"
)

everyday = extract(
    "    <!-- EVERYDAY TAB VIEW -->",
    "    <!-- APPLY TAB VIEW -->"
)

apply = extract(
    "    <!-- APPLY TAB VIEW -->",
    "    <!-- PLACEHOLDER PANELS FOR OTHER TABS -->"
)

other_tabs = extract(
    "    <!-- PLACEHOLDER PANELS FOR OTHER TABS -->",
    "  </div>\n\n  <!-- Bottom Navigation Bar -->"
)

bottom_navigation = extract(
    "  <!-- Bottom Navigation Bar -->",
    "\n\n</div>"
)

# Extract the Everyday account card into its own partial.
card_start_marker = (
    '        <div class="bg-white rounded-2xl shadow-xs '
    'border border-black/5 overflow-hidden">\n'
    '          <div class="p-5">'
)

card_end_marker = (
    "        </div>\n"
    "      </section>\n\n"
    '      <section class="bg-white rounded-2xl shadow-xs '
    'border border-black/5 overflow-hidden">'
)

card_start = everyday.find(card_start_marker)
card_end = everyday.find(card_end_marker, card_start)

if card_start == -1 or card_end == -1:
    raise ValueError("Could not locate the Everyday account card.")

card_closing = "        </div>\n"

account_card = everyday[
    card_start:card_end + len(card_closing)
]

everyday = (
    everyday[:card_start]
    + '        <%= render "accounts/account_card" %>\n'
    + everyday[card_end + len(card_closing):]
)

# Write the partial files.
files = {
    "app/views/shared/_top_navigation.html.erb": top_navigation,
    "app/views/home/_summary.html.erb": summary,
    "app/views/dashboards/_everyday.html.erb": everyday,
    "app/views/accounts/_account_card.html.erb": account_card,
    "app/views/home/_apply.html.erb": apply,
    "app/views/home/_other_tabs.html.erb": other_tabs,
    "app/views/shared/_bottom_navigation.html.erb": bottom_navigation,
}

for filename, content in files.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print(f"Created: {filename}")

# Replace the original index with the partial render structure.
index = '''<div data-controller="pill-nav" class="min-h-screen bg-[#F3F4F3] text-[#141716] pb-24">
  <div class="max-w-md mx-auto">
    <%= render "shared/top_navigation" %>
    <%= render "home/summary" %>
    <%= render "dashboards/everyday" %>
    <%= render "home/apply" %>
    <%= render "home/other_tabs" %>
  </div>

  <%= render "shared/bottom_navigation" %>
</div>
'''

source_path.write_text(index)
print("Updated: app/views/home/index.html.erb")
print("Refactoring complete.")
