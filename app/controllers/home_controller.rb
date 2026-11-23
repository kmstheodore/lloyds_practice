# app/controllers/home_controller.rb
class HomeController < ApplicationController
  def index
    @account = Account.first
    @remaining_overdraft = [ (@account.overdraft_limit + @account.balance), 0.to_d ].max
  end
end
