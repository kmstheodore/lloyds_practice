# db/seeds.rb
Account.find_or_create_by!(account_number: "32275668") do |a|
  a.name = "Classic"
  a.sort_code = "30-64-43"
  a.balance = -244.00
  a.overdraft_limit = 2000.00
  a.rewards_count = 63
end
