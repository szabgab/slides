require "spec"
require "../src/app"
describe "Try" do
  it "anagram" do
    anagram?("abc", "cba").should be_true
    anagram?("abc", "abd").should be_false
  end
end
