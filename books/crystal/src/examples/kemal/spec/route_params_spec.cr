ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/route_params"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<a href="/user/foo">/user/foo</a><br>})
    response.body.should_not contain(%{received})
  end

  it "renders /user/one" do
    get "/user/one"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should_not contain(%{<a})
    response.body.should contain(%{received fname: one})
  end

  it "renders /user/one/two" do
    get "/user/one/two"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should_not contain(%{<a})
    response.body.should contain(%{received fname: one and lname: two})
  end

  it "renders /user/one/two/three" do
    get "/user/one/two/three"
    response.status_code.should eq 200 # TODO should be 404
    response.headers["Content-Type"].should eq "text/html"
    response.body.should eq "" # TODO: where is the page?
  end

  it "renders /path/1/2/3/4/5" do
    get "/path/1/2/3/4/5"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should eq "received 1/2/3/4/5"
  end
end
