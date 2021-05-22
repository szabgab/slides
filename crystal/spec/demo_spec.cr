require "./spec_helper"

describe "demo test" do
  it "some free text here" do
    result = 23+19 # this might be calling the real application
    result.should eq 42
  end
end
