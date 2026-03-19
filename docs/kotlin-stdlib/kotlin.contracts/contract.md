

# contract

Specifies the contract of a function.

```kotlin
@ExperimentalContractsinline fun contract(builder: ContractBuilder.() -> Unit)(source)
```

```kotlin
import kotlin.contracts.*

@OptIn(ExperimentalContracts::class)
inline fun <T> T?.requireNotNull(): T {
    contract { returnsNotNull() implies (this@requireNotNull != null) }
    return this ?: throw IllegalArgumentException("value must not be null")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.contracts/contract.html)

    