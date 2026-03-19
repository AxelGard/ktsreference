

# plus

Returns a sequence containing all elements of the original sequence and then the given element.

```kotlin
operator fun <T> Sequence<T>.plus(element: T): Sequence<T>(source)
```

```kotlin
val original = sequenceOf("a", "b", "c")
val extended = original + "d"

println(extended.toList())   // prints [a, b, c, d]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/plus.html)

    