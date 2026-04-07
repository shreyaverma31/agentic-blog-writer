from graph.workflow import build_graph

app = build_graph()

topic = input("Enter blog topic: ")

result = app.invoke({
    "topic": topic
})

# Blue Sky Accord section
blue_sky_section = """
### International Alliances and the Blue Sky Accord

The Coalition of Liberty relies heavily on international alliances to provide strategic, logistical, and legal support in countering cyber-enabled insurgencies. Through shared intelligence, coordinated cyber defense protocols, and joint SOF operations, coalition members enhance the effectiveness and legitimacy of urban counter-insurgency efforts.

**Blue Sky Accord – Key Protocols:**

1. Collective Cyber Defense: Coalition members agree to deploy joint cyber defense mechanisms to neutralize threats from rogue states, including AI-driven countermeasures.
2. Autonomous Systems Oversight: All autonomous systems must comply with international humanitarian law, ensuring civilian protection and non-lethal principles.
3. Rapid Response Support: Rapid deployment of human and autonomous SOF units, mobile hospitals, and civil-military teams.
4. Containment and Escalation Management: Rogue states are contained through sanctions, cyber deterrence, and non-lethal operations before kinetic force.
5. Review and Accountability: Operations reviewed by a joint legal advisory board to ensure compliance with law and ethical standards.

> Expert Insight: “Treaties like the Blue Sky Accord exemplify how multilateral frameworks can provide both legitimacy and operational efficiency in high-risk urban environments,” notes Dr. Helena Meyer, specialist in military law and coalition operations.
"""

# Append to the final blog
result["final_blog"] += "\n\n" + blue_sky_section

# Print the final blog with the Blue Sky Accord section included
print("\n FINAL BLOG\n")
print(result["final_blog"])