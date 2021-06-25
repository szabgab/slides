def add(x, y)
    return x*y
end


describe "test cases" do
  it "good" do
    add(2, 2).should eq 4
  end

  pending "another test case when the bug is fixed"
  it "add" do
    add(2, 3).should eq 5
  end
  it "add" do
    add(2, 4).should eq 6
  end
end
