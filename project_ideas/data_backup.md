**Scope of the Project:**

The project aims to create a Python script that automatically backs up data from the system folders for Documents,
Downloads, Pictures, and Videos to an external drive. This script will ensure that important data is protected from
accidental deletion or hardware failures.

**Objectives:**

1. **Identify system folders for backup:** The script should determine the appropriate system folders to back up,
   including Documents, Downloads, Pictures, and Videos.

2. **Locate external drive:** The script should detect the connected external drive and ensure it is available for data
   transfer.

3. **Copy files from system folders to external drive:** The script should use the shutil module to recursively copy
   files and folders from the system folders to the external drive.

4. **Preserve file structure:** The script should maintain the original folder structure during the backup process.

5. **Inform user of backup progress:** The script should provide feedback to the user regarding the backup status,
   including estimated time remaining and any errors encountered.

6. **Schedule regular backups:** The script should be scheduled to run periodically to ensure that data is always
   protected.

7. **Handle large file sizes:** The script should handle large files efficiently, such as splitting them into smaller
   chunks if necessary.

8. **Maintain logs:** The script should create detailed logs to track backup history, including timestamps, file names,
   and any errors.

**Potential Extensions:**

1. **Differential backup:** Implement differential backups, which only copy files that have changed since the last full
   backup.

2. **Incremental backup:** Implement incremental backups, which copy files that have changed since the last full or
   incremental backup.

3. **Compression:** Consider compressing backup files to save storage space.

4. **Cloud storage integration:** Integrate with cloud storage services to provide additional backup options.

5. **User-friendly interface:** Develop a graphical user interface (GUI) for easier interaction with the backup script.