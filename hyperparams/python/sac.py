hyperparams = {
    "seals/HalfCheetah-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        batch_size=2048,
        buffer_size=100000,
        gamma=0.95,
        learning_rate=0.000884624878315995,
        policy_kwargs=dict(net_arch=[64, 64], log_std_init=-0.6932709443503001),
        tau=0.01,
        train_freq=64,
    ),
    "seals/Ant-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=1000,
        batch_size=512,
        buffer_size=1000000,
        gamma=0.98,
        learning_rate=0.0018514039303149058,
        policy_kwargs=dict(net_arch=[256, 256], log_std_init=-2.2692589009754176),
        tau=0.05,
        train_freq=64,
    ),
    "seals/Hopper-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=1000,
        batch_size=128,
        buffer_size=100000,
        gamma=0.98,
        learning_rate=0.001709807687567946,
        policy_kwargs=dict(net_arch=[256, 256], log_std_init=-1.6829391077276037),
        tau=0.08,
        train_freq=32,
    ),
    "seals/Walker2d-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=1000,
        batch_size=128,
        buffer_size=100000,
        gamma=0.99,
        learning_rate=0.0005845844772048097,
        policy_kwargs=dict(net_arch=[400, 300], log_std_init=0.1955317469998743),
        tau=0.02,
        train_freq=1,
    ),
    "seals/Humanoid-v0": dict(
        n_timesteps=2000000.0,
        policy="MlpPolicy",
        learning_starts=20000,
        batch_size=64,
        buffer_size=100000,
        gamma=0.98,
        learning_rate=4.426351861707874e-05,
        policy_kwargs=dict(net_arch=[400, 300], log_std_init=-0.1034412732183072),
        tau=0.08,
        train_freq=8,
    ),
    "seals/Swimmer-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=1000,
        batch_size=128,
        buffer_size=100000,
        gamma=0.995,
        learning_rate=0.00039981805535514633,
        policy_kwargs=dict(net_arch=[400, 300], log_std_init=-2.689958330139309),
        tau=0.01,
        train_freq=256,
    ),
}

# Add newer seals mujoco envs by copying the config from the old one
def is_mujoco_env(env: str):
    return any(mjenv in env for mjenv in
               ("Ant", "HalfCheetah", "Hopper", "Humanoid", "Swimmer", "Walker2d"))

hyperparams.update({
    env.replace("v0", "v1"): hyperparams[env] for env in hyperparams if is_mujoco_env(env)
})