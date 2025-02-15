const fs = require("fs");
const sqlite3 = require("sqlite3").verbose();

const dbFileName = "bug_reports.db";
let db;

function randomDate(start, end) {
    const date = new Date(
        start.getTime() + Math.random() * (end.getTime() - start.getTime())
    );
    return date.toISOString().slice(0, 10);
}

function initializeDatabase() {
    if (!fs.existsSync(dbFileName)) {
        db = new sqlite3.Database(dbFileName);
        db.serialize(() => {
            db.run(
                "CREATE TABLE bug_reports (\
                id INTEGER PRIMARY KEY NOT NULL,\
                category VARCHAR NOT NULL,\
                description TEXT NOT NULL,\
                severity VARCHAR NOT NULL,\
                cvss_score DECIMAL NOT NULL,\
                status VARCHAR NOT NULL,\
                reported_by VARCHAR NOT NULL,\
                reported_date DATE DEFAULT CURRENT_TIMESTAMP NOT NULL)"
            );
        });
        addSampleBugReports(db);
    } else {
        db = new sqlite3.Database(dbFileName);
    }
    return db;
}

function getBugReportById(id, callback) {
    const query = `SELECT * FROM bug_reports WHERE id=${id};`;
    db.get(query, function (error, result) {
        callback(error, result);
    });
}

function addSampleBugReports(db) {
    const reports = [
        {
            id: 1,
            category: "Authentication",
            description:
                "It is possible to bypass authentication by modifying the HTTP request.",
            severity: "High",
            cvss_score: 9.0,
            status: "Open",
            reported_by: "Alice",
        },
        {
            id: 2,
            category: "Input Validation",
            description:
                "The application does not properly sanitize input, leading to SQL injection.",
            severity: "High",
            cvss_score: 9.5,
            status: "Open",
            reported_by: "Bob",
        },
        {
            id: 3,
            category: "Cross-Site Scripting (XSS)",
            description:
                "A user can inject malicious code that will be executed by other users in their browsers.",
            severity: "Medium",
            cvss_score: 6.0,
            status: "Open",
            reported_by: "Charlie",
        },
        {
            id: 4,
            category: "Denial of Service (DoS)",
            description:
                "An attacker can crash the application by sending a specially crafted request.",
            severity: "High",
            cvss_score: 9.0,
            status: "Open",
            reported_by: "David",
        },
        {
            id: 5,
            category: "Information Disclosure",
            description:
                "Sensitive information is leaked in error messages returned by the application.",
            severity: "Low",
            cvss_score: 3.0,
            status: "Closed",
            reported_by: "Emily",
        },
        {
            id: 6,
            category: "Authorization",
            description:
                "A user can access resources they are not authorized to view or modify.",
            severity: "Medium",
            cvss_score: 5.5,
            status: "Open",
            reported_by: "Frank",
        },
        {
            id: 7,
            category: "Cryptographic Issues",
            description:
                "The application uses weak or insecure cryptographic algorithms.",
            severity: "High",
            cvss_score: 9.0,
            status: "Closed",
            reported_by: "Grace",
        },
        {
            id: 8,
            category: "Sensitive Data Exposure",
            description:
                "Sensitive data is stored unencrypted or unprotected on the server or in transit.",
            severity: "High",
            cvss_score: 9.2,
            status: "Closed",
            reported_by: "Henry",
        },
        {
            id: 9,
            category: "Session Management",
            description:
                "Session IDs are predictable or do not expire, allowing an attacker to hijack a session.",
            severity: "Medium",
            cvss_score: 5.8,
            status: "Open",
            reported_by: "Isabella",
        },
        {
            id: 10,
            category: "Business Logic",
            description:
                "The application does not properly enforce business logic rules, leading to fraudulent activity.",
            severity: "Low",
            cvss_score: 2.5,
            status: "Open",
            reported_by: "John",
        },
        {
            id: 11,
            category: "Weak Creds",
            description: "crypt0:c4tz on /4dm1n_z0n3, really?!",
            severity: "Critical",
            cvss_score: 10.0,
            status: "Open",
            reported_by: "ethical_hacker",
        },
    ];
    for (const report of reports) {
        const query = `INSERT INTO bug_reports (id, category, description, severity, cvss_score, status, reported_by, reported_date) VALUES (
         '${report.id}',
         '${report.category}',
         '${report.description}',
         '${report.severity}',
          ${report.cvss_score},
         '${report.status}',
         '${report.reported_by}',
         '${randomDate(new Date(2023, 0, 1), new Date())}')`;

        db.run(query, function (error) {
            if (error) {
                console.error("Error inserting bug report:", error.message);
            } else {
                console.log(`Bug report added with ID ${this.lastID}`);
            }
        });
    }
}

module.exports = {
    initializeDatabase,
    getBugReportById,
};
