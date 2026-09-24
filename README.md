# zepto-capstone
• Handling Missing / Corrupt Values: Dropping malformed rows rather than imputing was chosen to preserve raw catalog truth. For pricing and stock integrity in catalog indexing, fabricated numbers introduce downstream accounting risk.
• Currency Conversion: Fixed baseline of 1 GBP = 105.50 INR applied synchronously without external API latency or failure points.
• Normalization Schema: Category strings are isolated into a categories table to prevent string redundancy and reduce storage footprint across repeated records.
