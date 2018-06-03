echo firewall
vim-emu compute start -d vnfs_dc -n firewall -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.20/24),(id=output,ip=10.0.0.21/24)" -c "./start_firewall.sh 100 100 100 100 '128KB' 0 &"
echo parental-control
vim-emu compute start -d vnfs_dc -n parental-control -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.30/24),(id=output,ip=10.0.0.31/24)" -c "./start_snort.sh 100 100 100 100 '128KB' 0 &"
echo client-firewall
vim-emu network add -b -src client:client-eth0 -dst firewall:input
echo firewall-parental-control
vim-emu network add -b -src firewall:output -dst parental-control:input
echo parental-control-server
vim-emu network add -b -src parental-control:output -dst server:server-eth0
