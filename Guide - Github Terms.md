This guide translates the technical jargon of GitHub into clinical terms you already know. Think of this system not as "coding," but as a secure, collaborative charting system.

🏥 The Clinical Guide to "The System" (Git & GitHub)

We are building a shared brain for our practice. Because multiple NPs are adding guidelines at the same time, we need a way to track every change, prevent accidental deletions, and ensure everyone sees the same information.

Here is how the concepts map to your daily clinical life.
1. The Repository (Repo)
	Technical Term: Repository
	Clinical Analogy: The Central Medical Records Room
	 * What it is: The master folder that lives on the cloud (GitHub). It contains the "Source of Truth" for every guideline, policy, and image.
	 * How it works: You never "take" the original file. Instead, you have a Local Copy (Clone) on your own device. You can mess up your local copy all you want; the Central Records Room remains safe until you deliberately send your updates.
 
2. Stage
	Technical Term: Staging
	Clinical Analogy: The "To Be Signed" Pile
	 * The Concept: Imagine you have written notes for three different patients (Patient A, B, and C). You are finished with A and B, but C is still a draft.
	 * What Staging does: You "Stage" the notes for A and B. This puts them in a special pile that says, "These are ready to be finalized." Patient C’s note stays on your desk (Unstaged) and is not included in the batch you are about to sign.
	 * In Obsidian: Usually, the system automatically "Stages" all your changes for you. It grabs every file you edited and prepares them to be saved.
 
3. Commit
	Technical Term: Commit
	Clinical Analogy: Signing the Chart
	 * The Concept: A "Commit" is a permanent, time-stamped snapshot of your work. It is like signing your name at the bottom of a chart entry.
	 * The "Commit Message": When you sign, you attach a sticky note explaining what you did (e.g., "Updated Hypertension meds per JNC 8").
	 * Why it matters: This creates a Save Point. If you accidentally delete the entire Cardiology section next week, we can "rewind" the system to this exact Commit and restore the data.
	 * Key Rule: A Commit only saves the file on YOUR device. It hasn't been sent to the team yet.
 
4. Push
	Technical Term: Push
	Clinical Analogy: Faxing/Uploading to Central Records
	 * The Concept: You have "Committed" (Signed) ten chart entries today. They are official, but they are still sitting on your iPad. Nobody else can see them.
	 * What Pushing does: This takes your signed commits and uploads them to the Repository (GitHub).
	 * The Result: Once you "Push," the Wiki.js website updates, and the changes become visible to every other NP in the practice.
 
5. Pull (or Sync)
	Technical Term: Pull
	Clinical Analogy: Morning Handoff / Shift Report
	 * The Concept: While you were sleeping, the Night Shift NP added a new "Sepsis Protocol." If you start working now, your clipboard has old information.
	 * What Pulling does: Before you start writing, you "Pull" from the Repository. This downloads all the work your colleagues finished while you were away.
	 * Sync: A "Sync" is simply doing a Pull (get updates) followed immediately by a Push (send my updates).
 
⚡ Summary: The Cycle of a Clinical Note

| Term     | The "Nurse Speak" Translation                                                                                                              |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Clone    | Making a xerox copy of the entire chart rack to carry with you.                                                                            |
| Stage    | Stacking the finished papers together, ready for signature.                                                                                |
| Commit   | Signing the papers and stamping them with today's date.                                                                                    |
| Push     | Sending the signed papers to the Central Archive.                                                                                          |
| Pull     | Asking Central Records to give you the newest updates before you start rounds.                                                             |
| Conflict | Two nurses tried to write on the same line of the same chart at the same time. The system pauses and asks you: "Which version is correct?" |

💡 Why do we do this?
Why not just use Google Docs?
 * Safety: "Commits" allow us to undo mistakes instantly.
 * Ownership: We know exactly who wrote that guideline and when.
 * Offline: You can chart on the subway or in a hospital basement with no Wi-Fi. You just "Commit" offline, and "Push" when you get signal.
