import sys
sys.path.insert(0, r"e:\MathThon")

from Back_End.__init__ import create_app

app = create_app()
client = app.test_client()

with client.session_transaction() as sess:
    sess['admin_logged_in'] = True
    sess['username'] = 'Edward_Kenway'
    sess['role'] = 'admin'

res = client.get('/admin/export_database')
print(f"Status Code: {res.status_code}")
if res.status_code == 200:
    print(f"SUCCESS: Template rendered successfully ({len(res.data)} bytes)!")
else:
    print(f"FAILED: {res.status_code}")

# Test instant snapshot creation endpoint
res_snap = client.post('/admin/database/backup/create', json={'format': 'zip'})
print("Create snapshot response:", res_snap.status_code, res_snap.get_json())
