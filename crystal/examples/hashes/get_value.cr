person = {
   "name" => "Jane",
   "number" => 42,
}
puts person

# Unhandled exception: Missing hash key: "email" (KeyError)
# email = person["email"]
email = person["email"]?
puts email.nil? # true

name = person["name"]?
puts name # Jane

email = person["email"]? || "default@example.com"
puts email.nil? # false
puts email      # default@example.com

