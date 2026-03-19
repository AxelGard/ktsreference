

# toCollection

Appends all elements to the given destination collection.

```kotlin
@IgnorableReturnValuefun <T, C : MutableCollection<in T>> Array<out T>.toCollection(destination: C): C(source)
```

```kotlin
val array = arrayOf(1, 2, 3)
val list = mutableListOf<Int>()

array.toCollection(list)

println(list)   // Output: [1, 2, 3]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-collection.html)

    