require "digest/md5"

if ARGV.size != 1
    puts "Need EMAIL"
    exit 1
end

email = ARGV[0]
code = gravatar(email)
puts "https://www.gravatar.com/avatar/#{code}?s=100&d=blank"

def gravatar(email)
    return Digest::MD5.hexdigest(email)
end



