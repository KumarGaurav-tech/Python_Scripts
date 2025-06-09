import os
import time
import shutil

log_dir = "/var/log/gaurav"
archive_dir = "/var/log/gaurav/archive"
days_old = 7
cutoff = time.time() - (days_old * 86400)

os.makedirs(archive_dir, exist_ok=True)

for filename in os.listdir(log_dir):
 filepath = os.path.join(log_dir, filename)
 if os.path.isfile(filepath) and os.path.getmtime(filepath) < cutoff:
  shutil.move(filepath, os.path.join(archive_dir, filename))