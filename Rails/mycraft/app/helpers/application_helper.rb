module ApplicationHelper

  def gravatar_for(user, options = { size: 80 })
    username = Digest::MD5::hexdigest(user.chefname.downcase)
    size = options[:size]
    url = "https://crafatar.com/avatars/#{username}?overlay"
    image_tag(url, alt: user.chefname, class: "minecraft-skin", width: size, height: size)
  end

end
