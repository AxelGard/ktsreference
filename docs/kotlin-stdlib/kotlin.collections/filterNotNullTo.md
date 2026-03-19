

# filterNotNullTo

Appends all elements that are not null to the given destination.

```kotlin
@IgnorableReturnValuefun <C : MutableCollection<in T>, T : Any> Array<out T?>.filterNotNullTo(destination: C): C(source)
```

```kotlin
val nullableInts: Array<Int?> = arrayOf(1, null, 2, null, 3)
val nonNullList = mutableListOf<Int>()

nullableInts.filterNotNullTo(nonNullList)

println(nonNullList)   // Output: [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-not-null-to.html)

    