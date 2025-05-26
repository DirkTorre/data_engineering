# Data Engineering

I'm keeping this repo to keep track of everything related to data engineering.

I always liked the organising, cleaning, transforming and keeping track of data flow during my bio-informatics studies. So I want to improve on that.

The goals for now are:

- Learn polars for data manipulation, because op the better syntax and speed improvements compared to pandas.
- Learn dagster for data orchestration, which makes it easier to learn nextflow or snakemake in the future.
    + snakemake looks very easy, maybe just learn that and call it a day? but the job market for bio-info looks bad. 
    + nextflow is the way to go, but more difficult to learn.
    + **dagster** looks relatively easy, and can be used for all kinds of workflows.
    + airflow is the real deal for data engineering. difficult, but a requirement. i looked more into it, and it does not look THAT difficult, just a lot of code.
- Learn more about Postgress. Improve on my SQL skills

I'm gonna go with dagster, looks future proof and the most fun.
[Turns out some bio-info groups already use dagster](https://dagster.io/blog/zephyr-ai-case-study)

## choosing a tool for data orchestration 

- If you wanna go fast and easy for bio-info: go snakemake.
- If you want to be attractive as an bio-info engineer: go nextflow.
- if you wanna be able to always have a job: go airflow.
- if you want to learn 1 relatively easy tool for everything, go dagster.

Dagster is future proof on the long run and makes it easier for me to learn a bio-info alternative.

## idiot MS copilot helping me make a choice.

Currently, Apache Airflow is the most established tool in data orchestration, while Dagster is rapidly growing in popularity due to its modern approach. The demand for Nextflow and Snakemake, which cater to specific niche use cases, varies based on industry needs.

### Apache Airflow

Industry Standard: Airflow has been widely adopted since its introduction in 2014 and is considered the industry standard for data orchestration, often used in large-scale environments like Airbnb and Robinhood. Its extensive community support and existing library of plugins and connectors contribute to its ongoing demand 

Flexibility and Ecosystem: With a high degree of flexibility and a rich ecosystem of integrations (over 1,600 plugins), Airflow is ideal for teams needing robust, customizable solutions for complex workflows. Its proven scalability makes it suitable for organizations engaged in traditional ETL processes, data extraction, and report generation 

### Dagster

Emerging Competitor: Launched in 2019, Dagster is quickly gaining traction due to its asset-first approach, emphasizing data lineage and visibility. This modern tool offers built-in testing capabilities and improved ease of use for developing data pipelines, making it appealing for newer teams or those modernizing their data workflows 

Growing Demand: As more organizations prioritize data quality, testing, and developer productivity—and as the data landscape evolves—Dagster's capabilities resonate with those needs. It's particularly favored in data-centric organizations focusing on analytics and machine learning.

### Nextflow and Snakemake

Niche Demand: Both Nextflow and Snakemake are primarily used for bioinformatics and scientific data workflows. Demand for these tools tends to be more specialized, appealing to organizations in research, healthcare, and life sciences. They prioritize workflow reproducibility, making them popular among researchers needing high-quality analytical pipelines. However, their visibility in broader data engineering contexts is lesser compared to Airflow and Dagster.
Conclusion

### Conclusion

In summary, Apache Airflow remains the leader in data orchestration due to its established presence, flexibility, and extensive community support. Dagster, while newer, is gaining momentum as a viable alternative suited for modern workflows that focus on data quality and observability. The demand for Nextflow and Snakemake is more focused within specific scientific fields, which may show growth but is less mainstream in general data engineering roles.
By understanding these trends, teams can make informed decisions about which tools to focus on for their data orchestration needs, depending on their specific scenarios and industry requirements.
If you are looking for success in the data orchestration field, having skills in Apache Airflow and Dagster will likely benefit you significantly.

