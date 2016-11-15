# py_trigger

To run the playbook 

ansible-playbook trigger_py.yml -i hosts --extra-vars "cluster_nm='cluster\ 1' cm_host=hostname admin_id=admin admin_pass=admin" --ask-pass
