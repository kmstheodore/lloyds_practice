class CreateAccounts < ActiveRecord::Migration[8.1]
  def change
    create_table :accounts do |t|
      t.string :name
      t.string :sort_code
      t.string :account_number
      t.decimal :balance
      t.decimal :overdraft_limit
      t.integer :rewards_count

      t.timestamps
    end
  end
end
