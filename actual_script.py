fake = Faker()

# Configuration
TOTAL_RECORDS = 2825678  # Start with smaller number for testing
CHUNK_SIZE = 50000      # Process in chunks
OUTPUT_FILE = 'opay_customer_simulation.csv'

# Nigerian Names Data
NIGERIAN_FIRST_NAMES = [
    'Adebayo', 'Adeola', 'Adetokunbo', 'Adunni', 'Afolabi', 'Ajoke', 'Akeem', 'Aminat', 
    'Ayomide', 'Babajide', 'Bolanle', 'Busayo', 'Dolapo', 'Eniola', 'Fadekemi', 'Folasade',
    'Gbenga', 'Gbemisola', 'Idowu', 'Ireti', 'Jumoke', 'Kehinde', 'Kikelomo', 'Lanre',
    'Modupe', 'Morakinyo', 'Motunrayo', 'Muyiwa', 'Ngozi', 'Olabode', 'Oladele', 'Oladipo',
    'Olamide', 'Olanrewaju', 'Olasunkanmi', 'Olatunji', 'Oluwaseun', 'Oluwatoyin', 'Omolara',
    'Omowale', 'Opeyemi', 'Oyindamola', 'Segun', 'Seyi', 'Shade', 'Simisola', 'Taiwo', 'Adebayo', 'Adeola', 'Adetokunbo', 'Adunni', 'Afolabi', 'Ajoke', 'Akeem', 'Aminat', 
    'Ayomide', 'Babajide', 'Bolanle', 'Busayo', 'Dolapo', 'Eniola', 'Fadekemi', 'Folasade',
    'Gbenga', 'Gbemisola', 'Idowu', 'Ireti', 'Jumoke', 'Kehinde', 'Kikelomo', 'Lanre',
    'Modupe', 'Morakinyo', 'Motunrayo', 'Muyiwa', 'Ngozi', 'Olabode', 'Oladele', 'Oladipo',
    'Olamide', 'Olanrewaju', 'Olasunkanmi', 'Olatunji', 'Oluwaseun', 'Oluwatoyin', 'Omolara',
    'Omowale', 'Opeyemi', 'Oyindamola', 'Segun', 'Seyi', 'Shade', 'Simisola', 'Taiwo', 
    'Temitope', 'Titilayo', 'Yewande', 'Amarachi', 'Amobi', 'Chiamaka', 'Chibuzo', 'Chidiebere', 'Chidinma', 'Chiedozie', 'Chika',
    'Chike', 'Chimamanda', 'Chinasa', 'Chinelo', 'Chinenye', 'Chinonso', 'Chinwe', 'Chioma',
    'Chisom', 'Chukwudi', 'Chukwuemeka', 'Ebuka', 'Echezona', 'Ekene', 'Emeka', 'Emenike',
    'Ifeanyi', 'Ifeoma', 'Iheoma', 'Ikem', 'Ikenna', 'Kelechi', 'Ngozi', 'Nkechi', 'Nkiru',
    'Nnamdi', 'Nneka', 'Obioma', 'Ogechi', 'Ogechukwu', 'Okechukwu', 'Onyeka', 'Onyinye',
    'Tochukwu', 'Uchechi', 'Uchenna', 'Udoka', 'Ugonna', 'Uju', 'Uzoamaka', 'Yakubu', 'Zinachi', 'Aisha', 'Aminu', 'Auwal', 'Bilkisu', 'Binta', 'Dahiru', 'Fatima', 'Habiba',
    'Hadiza', 'Halima', 'Hauwa', 'Ibrahim', 'Idris', 'Jamila', 'Jibril', 'Kabiru',
    'Ladi', 'Lami', 'Lawan', 'Maryam', 'Muhammad', 'Mukhtar', 'Musa', 'Nafisa',
    'Nura', 'Rabiu', 'Rahama', 'Rashida', 'Sadiya', 'Safiya', 'Saidu', 'Salma',
    'Samira', 'Sani', 'Saratu', 'Shehu', 'Suleiman', 'Tijjani', 'Umar', 'Usman',
    'Yakubu', 'Yusuf', 'Zainab', 'Zara', 'Zubairu', 'Amina', 'Bello', 'Dauda',
    'Hassan', 'Jamil',  'Zoe', 'Michelle', 'David', 'Daniel', 'Grace', 'Joy', 'Victor', 'Peace',
    'Blessing', 'Favour', 'Precious', 'Goodness', 'Testimony', 'Happiness', 'Success',
    'Gift', 'Mercy', 'Patience', 'Glory', 'Praise', 'Winner', 'Destiny', 'Miracle',
    'Rejoice', 'ThankGod'
]

NIGERIAN_LAST_NAMES = [
    'Adeleke', 'Adesina', 'Adewale', 'Adeyemi', 'Afolayan', 'Agboola', 'Ajayi', 'Akinade',
    'Akinbola', 'Akingbade', 'Akinjide', 'Akinola', 'Akinsanya', 'Akintola', 'Alade', 'Balogun',
    'Bamgbose', 'Fagbemi', 'Fasola', 'Gbadebo', 'Idowu', 'Jaiyeola', 'Ogunlesi', 'Ogunleye',
    'Ogunmola', 'Ogunniyi', 'Ogunwale', 'Ojo', 'Okelola', 'Olanrewaju', 'Olatunji', 'Olawale', 'Adeleke', 'Adesina', 'Adewale', 'Adeyemi', 'Afolayan', 'Agboola', 'Ajayi', 'Akinade',
    'Akinbola', 'Akingbade', 'Akinjide', 'Akinola', 'Akinsanya', 'Akintola', 'Alade', 'Balogun',
    'Bamgbose', 'Fagbemi', 'Fasola', 'Gbadebo', 'Idowu', 'Jaiyeola', 'Ogunlesi', 'Ogunleye',
    'Ogunmola', 'Ogunniyi', 'Ogunwale', 'Ojo', 'Okelola', 'Olanrewaju', 'Olatunji', 'Olawale',
    'Oladeji', 'Oladele', 'Olaleye', 'Olaniran', 'Olowo', 'Oluwaseyi', 'Oni', 'Oyedepo',
    'Oyekanmi', 'Oyenuga', 'Oyewole', 'Salami', 'Sangodeyi', 'Soyinka', 'Taiwo', 'Talabi',
    'Williams', 'Yusuf',  'Achebe', 'Adichie', 'Agwu', 'Anyanwu', 'Eze', 'Ezenwa', 'Ibeh', 'Igbokwe',
    'Ihejirika', 'Iwu', 'Madu', 'Nwachukwu', 'Nwadike', 'Nwaeze', 'Nwafor', 'Nwagbo',
    'Nwankwo', 'Nwosu', 'Obi', 'Obioma', 'Ochi', 'Okafor', 'Okeke', 'Okonkwo',
    'Okorie', 'Okoro', 'Okoye', 'Okpara', 'Onyeka', 'Onyema', 'Uche', 'Uchendu',
    'Ude', 'Udechukwu', 'Udemezue', 'Umeh', 'Uzoma', 'Eke', 'Emeka', 'Ezeobi',
    'Ezeugwu', 'Ndukwe', 'Nwabueze', 'Nwaka', 'Nwoke', 'Nze', 'Obi', 'Offodile',
    'Ogbuagu', 'Okafor', 'Abubakar', 'Adamu', 'Ahmad', 'Bello', 'Danjuma', 'Dantata', 'Dikko', 'Garba',
    'Hassan', 'Ibrahim', 'Idris', 'Jibril', 'Kabiru', 'Lawan', 'Mohammed', 'Musa',
    'Mustapha', 'Sani', 'Shehu', 'Suleiman', 'Tukur', 'Umar', 'Usman', 'Yakubu',
    'Yusuf', 'Abdullahi', 'Aminu', 'Bala', 'Bashir', 'Dahiru', 'Galadima', 'Haruna',
    'Isah', 'Jafar', 'Kaita', 'Kano', 'Katsina', 'Maikano', 'Nuhu', 'Rabi',
    'Rilwanu', 'Salisu', 'Samaila', 'Sokoto', 'Tanko', 'Umaru', 'Yahaya', 'Zango',
    'Zaria', 'Zubairu', 'Egharevba', 'Edo', 'Erediauwa', 'Eweka', 'Igbinedion', 'Obaseki', 'Ogbemudia', 'Ogbomo',
    'Ogiemwonyi', 'Okojie', 'Okonjo', 'Okoro', 'Okunbor', 'Omoigui', 'Omorogbe', 'Omoruyi',
    'Osadebay', 'Oshiomhole', 'Ovia', 'Owamagbe', 'Owie', 'Ozolua', 'Uwaifo', 'Uzamere', 'YarAdua', 'Ade', 'Adebowale', 'Adegoke', 'Adekunle', 'Adeniyi', 'Aderemi', 'Adesanya', 'Adeyinka',
    'Afolabi', 'Ajao', 'Akande', 'Akin', 'Akinloye', 'Alabi', 'Awolowo', 'Babatunde',
    'Bankole', 'Fashola', 'Odedina', 'Odunayo', 'Ogunbayo', 'Ogunlana', 'Okafor', 'Okoro', 'Olowu'
]

# Nigerian states and regions
states = {
    'Abia': 'South East',
    'Adamawa': 'North East',
    'Akwa Ibom': 'South South',
    'Anambra': 'South East',
    'Bauchi': 'North East',
    'Bayelsa': 'South South',
    'Benue': 'North Central',
    'Borno': 'North East',
    'Cross River': 'South South',
    'Delta': 'South South',
    'Ebonyi': 'South East',
    'Edo': 'South South',
    'Ekiti': 'South West',
    'Enugu': 'South East',
    'FCT (Abuja)': 'North Central',
    'Gombe': 'North East',
    'Imo': 'South East',
    'Jigawa': 'North West',
    'Kaduna': 'North West',
    'Kano': 'North West',
    'Katsina': 'North West',
    'Kebbi': 'North West',
    'Kogi': 'North Central',
    'Kwara': 'North Central',
    'Lagos': 'South West',
    'Nasarawa': 'North Central',
    'Niger': 'North Central',
    'Ogun': 'South West',
    'Ondo': 'South West',
    'Osun': 'South West',
    'Oyo': 'South West',
    'Plateau': 'North Central',
    'Rivers': 'South South',
    'Sokoto': 'North West',
    'Taraba': 'North East',
    'Yobe': 'North East',
    'Zamfara': 'North West'
}


occupations = [
    'Student', 'Trader', 'Civil Servant', 'Business Owner', 'Freelancer',
    'Professional', 'POS Agent', 'Artisan', 'Driver', 'Farmer'
]

payment_methods = ['Mobile App', 'USSD', 'Agent Network', 'Card Payment']
payment_plans = [
    'Daily Savings',
    'Weekly Savings',
    'Monthly Savings',
    'School Fees Plan',
    'Rent Plan',
    'Car Savings',
    'Travel Holiday Savings',
    'Investment Plan',
    'Emergency Fund'
]

# Function to assign income based on occupation
def assign_income(occupation):
    if occupation == 'Student':
        return np.random.randint(50000, 99999)
    elif occupation == 'Trader':
        return np.random.randint(100000, 500000)
    elif occupation in ['Business Owner', 'Professional']:
        return np.random.randint(150000, 800000)
    elif occupation == 'POS Agent':
        return np.random.randint(120000, 600000)
    elif occupation == 'Civil Servant':
        return np.random.randint(80000, 300000)
    else:
        return np.random.randint(50000, 300000)

def generate_opay_customer_data(num_records):
    """Generate complete OPay customer dataset"""
    data = []
    start_time = time.time()
    
    for i in range(num_records):
        # Generate Nigerian identity
        first_name = random.choice(NIGERIAN_FIRST_NAMES)
        last_name = random.choice(NIGERIAN_LAST_NAMES)
        state = random.choice(list(states.keys()))
        occupation = random.choice(occupations)
        income = assign_income(occupation)
        
        # Generate contact info
        phone_prefix = random.choice(['080', '081', '090', '070', '091'])
        phone_number = phone_prefix + ''.join([str(random.randint(0, 9)) for _ in range(8)])
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(10,99)}@{fake.free_email_domain()}"
        
        # Create customer record
        record = {
            'customer_id': fake.uuid4(),
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'age': random.randint(18, 70),
            'gender': random.choices(['Male', 'Female'], weights=[0.55, 0.45])[0],
            'state': state,
            'region': states[state],
            'urban_rural': random.choices(['Urban', 'Rural'], weights=[0.7, 0.3])[0],
            'occupation': occupation,
            'monthly_income': income,
            'primary_bank': 'OPay',
            'account_type': random.choice(['OPay Wallet', 'Virtual Account']),
            'has_bvn': random.random() < 0.9,
            'transaction_frequency': random.randint(1, 45),
            'avg_transaction_amount': round(income * random.uniform(0.01, 0.2)),
            'last_transaction_date': fake.date_between(start_date='-3m', end_date='today'),
            'account_creation_date': fake.date_between(start_date='-4y', end_date='today'),
            'device_type': random.choices(['Android', 'iOS', 'Feature Phone'], weights=[0.7, 0.15, 0.15])[0],
            'network_provider': random.choices(['MTN', 'Airtel', 'Glo', '9mobile'], weights=[0.5, 0.3, 0.15, 0.05])[0]
        }
        data.append(record)
        
        # Show progress every CHUNK_SIZE records
        if i > 0 and i % CHUNK_SIZE == 0:
            elapsed = time.time() - start_time
            print(f"Generated {i:,}/{num_records:,} records ({i/num_records:.1%})")
    
    return pd.DataFrame(data)

# Generate data
print(f"Generating {TOTAL_RECORDS:,} OPay customer records...")
df = generate_opay_customer_data(TOTAL_RECORDS)
df.to_csv(OUTPUT_FILE, index=False)

print(f"\nCompleted! Saved {len(df):,} records to {OUTPUT_FILE}")
print("\nSample data:")
print(df[['first_name', 'last_name', 'state', 'occupation', 'monthly_income']].head(3))
