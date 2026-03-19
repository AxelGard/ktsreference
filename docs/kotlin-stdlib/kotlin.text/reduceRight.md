

# reduceRight

Accumulates value starting with the last character and applying operation from right to left to each character and current accumulator value.

```kotlin
inline fun CharSequence.reduceRight(operation: (Char, acc: Char) -> Char): Char(source)
```

```kotlin
val source = "kotlin"
val reversed = source.reduceRight { c, acc -> acc + c }
println(reversed) // prints "niltok"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-right.html)

    