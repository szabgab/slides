ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/post_params"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="POST" action="/">})
    response.body.should_not contain(%{You typed in <b>})
  end

  it "renders / POST text=Foo Bar" do
    post "/", body: "text=Foo Bar", headers: HTTP::Headers{"Content-Type" => "application/x-www-form-urlencoded"}
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{<form method="POST" action="/">})
    response.body.should contain(%{You typed in <b>Foo Bar</b>})
  end
end
