VAGRANT_API_VERSION = "2"

$script = <<SCRIPT
  export DEBIAN_FRONTEND=noninteractive
  echo apt-get update
  apt-get update -qq

  echo install buil-essential python3-pip python3-dev libssl-dev cargo
  apt-get install build-essential python3-pip python-dev libssl-dev cargo -qq

  echo install the mysql client libraries
  apt-get install default-mysql-client libmysqlclient-dev -qq

  echo install ansible
  python3 -m pip install ansible
  python3 -m pip install --upgrade pip

  # export ANSIBLE_CONFIG="/srv/dashboard-backend/ansible/ansible.cfg"
  cd /srv/dashboard-backend/ansible
  ansible-playbook vagrant.yml -i hosts --connection=local
  # cat /vagrant/ident
SCRIPT

Vagrant.configure(VAGRANT_API_VERSION) do |config|
  config.ssh.insert_key = false
  config.vm.define "focal64", primary: true do |focal|
    focal.vm.box = "ubuntu/focal64"
    focal.vm.network :forwarded_port, guest: 8051, host: 8041 # Expose API
    focal.vm.network :forwarded_port, guest: 3031, host: 3031
    focal.vm.network :forwarded_port, guest: 3306, host: 3307
    focal.vm.synced_folder "", "/srv/dashboard-backend", :owner=>"vagrant", :group=>"vagrant", :mount_options=>["dmode=777", "fmode=777"]
    focal.vm.provision :shell, :inline => $script, env: { "ANSIBLE_STDOUT_CALLBACK" => 'yaml' }
    focal.vm.provider "virtualbox" do |v|
      v.gui = true
      v.memory = 4192
      v.cpus = 4
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
  end
end
