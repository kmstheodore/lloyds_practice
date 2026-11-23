# app/helpers/application_helper.rb
module ApplicationHelper
  def gbp(amount)
    val = amount.to_d
    formatted = number_with_delimiter(format("%.2f", val.abs))
    val.negative? ? "-£#{formatted}" : "£#{formatted}"
  end
end
