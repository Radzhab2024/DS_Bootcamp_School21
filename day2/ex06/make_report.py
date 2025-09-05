from analytics import Research
from config import num_of_steps, report_template

path_to_file = 'data.csv'

try:
    research = Research(path_to_file)
    file_content = research.file_reader()
    print(file_content)

    analytics = Research.Analytics(file_content)

    heads_sum, tails_sum = analytics.counts()
    print(heads_sum, tails_sum)

    heads_percentage, tails_percentage = analytics.fractions(heads_sum, tails_sum)
    print(heads_percentage, tails_percentage)

    predictions = analytics.predict_random(num_of_steps)
    predicted_heads = sum(predict[0] for predict in predictions)
    predicted_tails = sum(predict[1] for predict in predictions)

    report = report_template.format(
        observations=len(file_content),
        tails=tails_sum,
        heads=heads_sum,
        tails_percent=tails_percentage,
        heads_percent=heads_percentage,
        steps=num_of_steps,
        predicted_tails=predicted_tails,
        predicted_heads=predicted_heads
    )

    analytics.save_file(report, "report")
    print("Report saved to report.txt")

except Exception as e:
    print(f"Error: {e}")
