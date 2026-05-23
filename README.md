# IPT_Mod4_Lab4.1

A Lab activity to satisfy the following Problem Scenario:
**develop a Secure Student Records API**

---

### 🔐 1. Authenticate users using JWT
All users must prove their identity to access the system.

**Student Auth:**
<img width="1920" height="1080" alt="Screenshot (1836)" src="https://github.com/user-attachments/assets/7b33abd5-b0a8-4402-b93b-dc2ad16efa7c" />


---

### 👑 2. Allow only Admins to create or delete student records
Admins have full control over the database.

**Admin successful creation of student record:**
<img width="1920" height="1080" alt="Screenshot (1849)" src="https://github.com/user-attachments/assets/d8ece7e9-df5d-4f8c-82e5-42d1c057bcd3" />


**Admin successful account deletion:**
<img width="1920" height="1080" alt="Screenshot (1857)" src="https://github.com/user-attachments/assets/fe633a24-b7b7-4843-849b-d1da204f152c" />


**Faculty (or students) unable to add or delete a student record:**
* **Acc deletion denial:** <img width="1920" height="1080" alt="Screenshot (1863)" src="https://github.com/user-attachments/assets/b0996db5-2ed7-40d2-8444-dede1f02e27a" />


---

### 👨‍🏫 3. Allow Faculty to view and update records
Teachers can see student files and update information (like changing a course), but cannot enroll or expel students.

**Faculty Auth:**
<img width="1920" height="1080" alt="Screenshot (1860)" src="https://github.com/user-attachments/assets/6096cd35-36cd-4507-ab59-8e73aede82d4" />


**Faculty editing record (Before):**
<img width="1920" height="1080" alt="Screenshot (1862)" src="https://github.com/user-attachments/assets/a6e15280-0658-405c-a66b-a9103bf36b70" />


**Faculty editing record (After):**
<img width="1920" height="1080" alt="Screenshot (1864)" src="https://github.com/user-attachments/assets/0213027a-f368-45a6-9449-2617b399d636" />


---

### 🎓 4. Allow students to view only their own record
Strict privacy rules are enforced so students cannot snoop on each other's grades or files.

**Student Auth:**
<img width="1920" height="1080" alt="Screenshot (1865)" src="https://github.com/user-attachments/assets/3de21f9b-8874-4d3a-b904-d442546890ef" />

**Student 1 can view their record:**
<img width="1920" height="1080" alt="Screenshot (1866)" src="https://github.com/user-attachments/assets/c4b2bfae-3b61-4044-a045-5c5701e1916f" />


**But can't view or get Student 2's:**
<img width="1920" height="1080" alt="Screenshot (1867)" src="https://github.com/user-attachments/assets/62d65b94-e392-478f-a3b4-64edb49951d1" />
