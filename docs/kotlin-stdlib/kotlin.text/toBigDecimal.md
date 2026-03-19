

# toBigDecimal

Parses the string as a java.math.BigDecimal number and returns the result.

```kotlin
inline fun String.toBigDecimal(): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val numberString = "9876.54321"
    val bigDecimal = numberString.toBigDecimal()
    println("BigDecimal value: $bigDecimal")  // prints: BigDecimal value: 9876.54321
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-big-decimal.html)

    