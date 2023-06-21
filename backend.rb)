# Save this code in backend.rb
require 'sinatra'
require 'faye'

set :public_folder, 'public'

shared_content = ''

get '/' do
  erb :index
end

faye_server = Faye::RackAdapter.new(mount: '/faye', timeout: 25)
run faye_server

Faye::WebSocket.load_adapter('thin')

faye_server.add_extension(SharedContentExtension.new(shared_content))

class SharedContentExtension
  def initialize(shared_content)
    @shared_content = shared_content
  end

  def incoming(message, callback)
    if message['channel'] == '/shared-content'
      message['data'] = @shared_content
    end

    callback.call(message)
  end

  def outgoing(message, callback)
    if message['channel'] == '/shared-content'
      @shared_content = message['data']
    end

    callback.call(message)
  end
end
