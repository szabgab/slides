require "spec"
require "./mymath.cr"

describe "add" do
  it "correctly adds two numbers" do
    add(2, 2).should eq 4
  end
end

describe "add" do
  it "correctly adds two numbers" do
    add(2, 3).should eq 5
  end
end

# describe Array do
#   describe "#size" do
#     it "correctly reports the number of elements in the Array" do
#       [1, 2, 3].size.should eq 3
#     end
#   end

#   describe "#empty?" do
#     it "is true when no elements are in the array" do
#       ([] of Int32).empty?.should be_true
#     end

#     it "is false if there are elements in the array" do
#       [1].empty?.should be_false
#     end
#   end
# end
