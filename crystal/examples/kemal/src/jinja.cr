require "kemal"
require "crinja"

get "/" do
  crinja = Crinja.new
  crinja.loader = Crinja::Loader::FileSystemLoader.new("src/views/")

  template = crinja.get_template("home.html.j2")
  template.render({
    "title"   => "With CRinja",
    "planets" => ["Mercury", "Venus", "Earth", "Mars"],
    "cond"    => Random.new.next_bool,
  })
end

Kemal.run
