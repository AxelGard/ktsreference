

# value

The value of this variable.

```kotlin
var <T : Boolean> BooleanVarOf<T>.value: T(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    // Create a BooleanVarOf with an initial value of true
    val boolVar = BooleanVarOf(true)

    // Read the current value
    println("Initial value: ${boolVar.value}")

    // Update the value to false
    boolVar.value = false
    println("After update: ${boolVar.value}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/value.html)

    