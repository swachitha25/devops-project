# Incident Post-Mortem: API Latency and Timeout Errors

## Incident Summary
On [date], a production API service experienced a significant increase in response latency during peak traffic hours. Average response times increased from approximately 200ms to 3000ms, and around 5% of requests resulted in 504 Gateway Timeout errors. The incident lasted for approximately 45 minutes before full service recovery.

## Timeline of Events
- T+00 min: Increased latency observed in application dashboards during peak traffic.
- T+05 min: Customer-facing errors reported by monitoring alerts and internal teams.
- T+10 min: On-call engineer acknowledged the incident and began investigation.
- T+20 min: Initial analysis pointed to elevated pod restarts and resource pressure.
- T+30 min: Mitigation actions applied, including scaling adjustments.
- T+45 min: Service stabilized and error rates returned to baseline levels.

## Root Cause Analysis
The root cause was resource exhaustion in the Kubernetes cluster caused by underestimated memory requests for API pods. During traffic spikes, pods exceeded memory limits and were restarted, leading to request retries and cascading latency. This was compounded by uneven traffic distribution across replicas.

## Monitoring and Alerting Gaps
While latency alerts were triggered, there were no early warnings for memory pressure or pod restarts at the service level. Alerts were reactive rather than predictive, delaying identification of the underlying issue.

## Remediation Actions
- Increase memory requests and limits based on observed usage (High priority)
- Improve Horizontal Pod Autoscaler thresholds to react earlier to traffic spikes (High priority)
- Add alerts for pod restart rates and memory saturation (Medium priority)
- Review load balancing and readiness probe configuration (Medium priority)

## Preventive Measures
To prevent recurrence, resource sizing will be reviewed regularly using historical metrics. Additional dashboards will be created to track pod stability, memory usage, and request latency. Load testing will also be incorporated into pre-production environments to better simulate peak traffic scenarios.

## Proposed Monitoring Improvements
New dashboards will include:
- API latency percentiles (P50, P95, P99)
- Pod restart counts
- Memory and CPU utilization per pod
- Error rate by status code

Alerts will be configured to trigger on sustained memory pressure and abnormal restart patterns, enabling faster and more proactive incident response.
