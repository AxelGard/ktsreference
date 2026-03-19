

# filterNotNull

Returns a sequence containing all elements that are not null.

```kotlin
fun <T : Any> Sequence<T?>.filterNotNull(): Sequence<T>(source)
```

```kotlin
val numbers: Sequence<Int?> = sequenceOf(1, null, 3, null, 5)

val nonNullNumbers: Sequence<Int> = numbers.filterNotNull()

println(nonNullNumbers.toList()) // Output: [1, 3, 5]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-not-null.html)

    