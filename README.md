# UFC Fight Prediction

## Project Overview
This project analyzes data from the Ultimate Fighting Championship (UFC) to build machine learning models for predicting the outcomes of future fights. The primary objective is to achieve high accuracy in predicting fight outcomes based on fighter attributes. The current model demonstrates an impressive 83% accuracy rate.

## Project Structure
- `Data`: This directory contains the raw data used to create a SQL database and data used to test the model
- `Notebooks`: Jupyter notebooks used for pre-processing, exploratory analysis, model building and testing
- `trained_model.pkl`: The trained Random Forest model
- `.gitignore`: The files to be ignored

## Important Fighter Features
- Ht.: Height
- Wt.: Weight
- Open Stance: The feet are spaced wider with the front toe toward the opponent and the rear foot at 45 degrees
- Orthodox: Fighters stand with their left foot in front and their right foot in the back. Right hand is connected to the chin or head, while the left hand is in the lead.
- Southpaw: Fighter has the right hand and the right foot forward, leading with right jabs, and following with a left cross right hook. It is the normal stance for a left-handed boxer.
- Sideways: Any guard in which the front foot is turned inward.
- Switch: Fighter switches between different stances.
- W: Win
- L: Loss
- D: Draw
- Kd: Knock-down rate per 15min in fight
- Str: Number of Significant Strikes in fight
- Td: Number of Take-downs per 15min in fight
- Sub: Number of Submissions per 15min in fight
- sig_str_pm: Significant Strikes per minute (fighter stats)
- str_acc_percentage: % Strike Accuracy (fighter stats)
- str_abs_pm: Significant Strikes Absorbed per minute (fighter stats)
- str_def_percentage: % Strikes Defended Against (fighter stats)
- td_acc_percentage: % Take-down Accuracy (fighter stats)
- td_def_percentage: % Take-downs Defended Against (fighter stats)

## Weight Classes
- Women's Strawweight: 115 lbs>
- Flyweight: 125 lbs>
- Bantamweight: 135 lbs>
- Featherweight: 145 lbs>
- Lightweight: 155 lbs>
- Welterweight: 170 lbs>
- Middleweight: 185 lbs>
- Light Heavyweight: 205 lbs>
- Heavyweight: 265 lbs>
- Super Heavyweight: 265 lbs< (not yet officially recognized)

## Model Performance
So far, the model has achieved an 83% accuracy rate in predicting fight outcomes and has only continued to improve each week.

## Contributing
This project is not intended for others to run, but if you have any feedback, questions, or ideas related to this project, please feel free to reach out to me!

## Contact Information
- LinkedIn Profile: www.linkedin.com/in/sagehalewolfe
