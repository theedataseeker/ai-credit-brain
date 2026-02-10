# main.py

from economy.population import load_population
from economy.loan_simulator import run_monthly_simulation
from economy.cashflow import calculate_monthly_profit


def main():
    print("Starting AI Credit Brain Simulation...")

    # 1. Load synthetic population
    population_df = load_population("check")#file_path="data/synthetic/population.csv"

    print(f"Population loaded: {len(population_df)} users")

    # 2. Initialize empty loan book
    loan_book = []

    # 3. Run one month simulation
    simulation_result = run_monthly_simulation()
    #     population=population_df,
    #     loan_book=loan_book,
    #     month=1
    # )

    # 4. Calculate profit
    profit_metrics = calculate_monthly_profit() #simulation_result
    profit_metrics['net_profit'] = profit_metrics['interest_earned'] - profit_metrics['defaults']
    profit_metrics['npa_pct'] = (profit_metrics['defaults']*100)/profit_metrics['principal_disbursed']
    print(type(profit_metrics))
    # 5. Print results
    print("\n--- Month 1 Results ---")
    print(f"Loans Disbursed : {profit_metrics['loans_disbursed']}")
    print(f"Total Principal : ₹{profit_metrics['principal_disbursed']:,.0f}")
    print(f"EMI Collected   : ₹{profit_metrics['emi_collected']:,.0f}")
    print(f"Interest Earned: ₹{profit_metrics['interest_earned']:,.0f}")
    print(f"Defaults Amount: ₹{profit_metrics['defaults']:,.0f}")
    print(f"Net Profit     : ₹{profit_metrics['net_profit']:,.0f}")
    print(f"NPA %          : {profit_metrics['npa_pct']:.2f}%")

    print("\nSimulation completed successfully.")


if __name__ == "__main__":
    main()
