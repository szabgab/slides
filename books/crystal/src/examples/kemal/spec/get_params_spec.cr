ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/get_params"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="GET" action="/">})
    response.body.should_not contain(%{You typed in <b>})
  end

  it "renders /?text=Foo Bar" do
    get "/?text=Foo Bar"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="GET" action="/">})
    response.body.should contain(%{You typed in <b>Foo Bar</b>})
  end
end
