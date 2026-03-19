

# sumOf

Returns the sum of all values produced by selector function applied to each character in the char sequence.

```kotlin
@JvmName(name = "sumOfDouble")inline fun CharSequence.sumOf(selector: (Char) -> Double): Double(source)
```

```kotlin
val text = "abc"
val sum = text.sumOf { it.code.toDouble() }   // 97.0 + 98.0 + 99.0 = 294.0
println("The sum of the character codes is $sum")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/sum-of.html)

    