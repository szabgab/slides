ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/params"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="POST" action="/user/foobar?email=foo@bar.com">})
  end

  it "renders mixed POST request" do
    post "/user/foobar?email=foo@bar.com", body: "text=Foo Bar", headers: HTTP::Headers{"Content-Type" => "application/x-www-form-urlencoded"}
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="POST" action="/user/foobar?email=foo@bar.com">})
    response.body.should contain(%{<div>route: foobar</div>})
    response.body.should contain(%{<div>get: foo@bar.com</div>})
    response.body.should contain(%{<div>post: Foo Bar</div>})
  end
end
