# FROM python:3.12-slim

# WORKDIR /home/sante/Документы/my_projects/NyxMetrics

# # install poetry
# RUN pip install poetry

# # install libgl/linux
# RUN pip install libGL

# # copy poetry files
# COPY pyproject.toml poetry.lock ./  

# RUN poetry config virtualenvs.create false 

# RUN poetry install --no-interaction --no-root

# COPY . .

# CMD [ "python", "main.py" ]