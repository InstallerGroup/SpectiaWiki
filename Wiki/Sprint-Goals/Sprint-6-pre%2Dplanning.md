To ensure the prearation of the relevant UX and BE stories for the Sprint 6 planning on Tuesday, 12.11. we had a session about the overall priorities for next sprint (Mark, Henrik, Jakob, Claudia):

## **Priority 1: Invoice Control**
We agreed that invoice control should have the following tasks completed before UAT for end users is meaningful. Main focus is to have the data for first wholesaler (AO) working correctly before other wholesaler data is added. Tasks are in prioritized order:
1. Total amount in sticky header updates automatically based on changes in date range, or removal of invoice errors #3332
1. Bonus to be calculated correctly on invoice control. @<F1B17662-B773-6975-B1A2-48927F7D9691>  is currently investigating how AO has calculated the bonus to understand if we need to do any adjustments in our implementation (eta 08.11.). @<0EBA20A6-5B36-475E-9536-CC042704399F>  will describe the user story for the potential changes on monday to have it reviewed and agreed with Mark by Tuesday, 12.11. #3427
1. FE to implement the design review (see sticky header bug and sticky on advanced view missing) #3443 #3066
1. FE to implement the locking of lines that depend on investigations #3066
1. FE to implement the comment feature on advanced view #3066
1. FE to implement receipt page #3426
1. Enabling feature to export excel file with invoice errors to start "Returkrav" #3185

Other tasks that are needed for extended UAT testing:
- LM #2380, BD #2379 data are available

Nice to have feature, not required for UAT of version 1:
- Calculate bonus (we have to agree where this belongs in the UI, most likely part of analytics EPIC) Should this be documented here? #3317


## **Priority 2: Implement compare wholesaler**
Since this feature is discussed to provide more immediate value for the end user, we switched priority to this feature instead of doing material list first. We evaluated that material list is first adding actual value once the PIM system is implemented and data can be shown in Spectia. 
Next step:
1. @<F1B17662-B773-6975-B1A2-48927F7D9691>  will share the examples of the current excel files with Henrik #3440
2. @<0EBA20A6-5B36-475E-9536-CC042704399F>  to create a template that we will request the wholesalers to use for returning their proposal to IG (incl. 4 key columns and the indication of replaced products) #3441
3. @<0EBA20A6-5B36-475E-9536-CC042704399F>, @<F5E3506F-4E89-4094-A31E-24BBA8CD9AA6> and @<F1B17662-B773-6975-B1A2-48927F7D9691> to plan a deep dive to specify compare wholesaler requirements on Tuesday, 12.11. after planning.
4. @<0EBA20A6-5B36-475E-9536-CC042704399F> will add stories to the ongoing sprint 6 by Thursday/Friday, once the review is completed by Mark
5. Until compare wholesalers is ready to be picked up by BE, Rasmus will help with code review, invoice control completion where possible and setup of UAT environment. @<0EBA20A6-5B36-475E-9536-CC042704399F> will brief Rasmus. Note I cannot tag him here for some reason.


## **Priority 3: Material list**
Value will be added, once PIM is in place. 
1. @<5D67D5D3-810C-4486-97ED-FFA97AC5334A> will create a process- and timeplan, once @<4F1564BF-D3C3-4068-AAF2-B5150446F047>  shared the contact of PIM-Søren from Århus

See drawing on white board below:
![Image.jpg](/.attachments/Image-26a0ca9a-d09a-4125-944d-67341c9421c9.jpg)








