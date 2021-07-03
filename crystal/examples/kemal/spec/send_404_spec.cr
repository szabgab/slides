ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/send_404"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<a href="/user/foo">/user/foo</a><br>})
    response.body.should_not contain(%{received})
  end

  it "renders /user/foo" do
    get "/user/foo"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{received fname: foo})
  end

  it "renders /user/bar" do
    get "/user/bar"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{received fname: bar})
  end

  it "renders /user/other" do
    get "/user/other"
    response.status_code.should eq 404
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{We don't have this user <b>other</b>})
  end
end
